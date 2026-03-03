// ============================================================
// Quantum Step — Google Apps Script v3
// Lead Logger + Calculation Logger + Full Telemetry
// ============================================================
//
// SETUP:
//   1. script.google.com → paste this code → Save
//   2. Deploy → Manage Deployments → Edit → New version → Deploy
//   3. Keep the same URL — all tool files already have it
//
// SHEETS CREATED AUTOMATICALLY:
//   • "Leads"        — who opened the tool (name, device, IP, location...)
//   • "Calculations" — what they calculated (inputs + results + telemetry)
// ============================================================

var LEAD_SHEET_NAME = 'Leads';
var CALC_SHEET_NAME = 'Calculations';

// Ordered columns for the Leads sheet
var LEAD_COLS = [
  'Timestamp (IST)', 'Name', 'Email', 'Tool', 'URL', 'Referrer',
  'IP', 'City', 'Region', 'Country', 'ISP', 'Latitude', 'Longitude',
  'Device Type', 'OS', 'Browser', 'Screen', 'Viewport',
  'Language', 'Timezone', 'Connection',
  'UTM Source', 'UTM Medium', 'UTM Campaign', 'User Agent'
];

// Fixed columns for the Calculations sheet (dynamic input/result cols added after)
var CALC_FIXED_COLS = [
  'Timestamp (IST)', 'Name', 'Email', 'Tool', 'URL',
  'IP', 'City', 'Country', 'Device Type', 'OS', 'Browser'
];

function doPost(e) {
  try {
    var payload = JSON.parse(e.postData.contents);
    var ss = SpreadsheetApp.getActiveSpreadsheet();
    if (payload.type === 'calculation') {
      writeCalculation(ss, payload);
    } else {
      writeLead(ss, payload);
    }
    return ContentService
      .createTextOutput(JSON.stringify({ status: 'ok' }))
      .setMimeType(ContentService.MimeType.JSON);
  } catch (err) {
    return ContentService
      .createTextOutput(JSON.stringify({ status: 'error', msg: err.toString() }))
      .setMimeType(ContentService.MimeType.JSON);
  }
}

// ─── Leads ───────────────────────────────────────────────────────────────────
function writeLead(ss, d) {
  var sheet = getOrCreateSheet(ss, LEAD_SHEET_NAME, LEAD_COLS);
  var tel = d.telemetry || {};
  sheet.appendRow([
    toIST(d.timestamp),
    d.name || '',
    d.email || '',
    d.tool || '',
    d.url || '',
    d.referrer || tel.referrer || 'direct',
    tel.ip || '',
    tel.city || '',
    tel.region || '',
    tel.country || '',
    tel.isp || '',
    tel.lat || '',
    tel.lon || '',
    tel.device_type || '',
    tel.os || '',
    tel.browser || '',
    tel.screen || '',
    tel.viewport || '',
    tel.language || '',
    tel.timezone || '',
    tel.connection || '',
    tel.utm_source || '',
    tel.utm_medium || '',
    tel.utm_campaign || '',
    tel.user_agent || ''
  ]);
}

// ─── Calculations ─────────────────────────────────────────────────────────────
function writeCalculation(ss, d) {
  var calcData = d.data || {};
  var inputs = calcData.inputs || {};
  var results = calcData.results || {};
  var tel = d.telemetry || {};

  var inputKeys = Object.keys(inputs);
  var resultKeys = Object.keys(results);

  var allHeaders = CALC_FIXED_COLS.concat(
    inputKeys.map(function (k) { return 'in_' + k; }),
    resultKeys.map(function (k) { return 'out_' + k; })
  );

  var sheet = getOrCreateSheet(ss, CALC_SHEET_NAME, allHeaders);
  ensureHeaders(sheet, allHeaders);

  var headerRow = sheet.getRange(1, 1, 1, sheet.getLastColumn()).getValues()[0];
  var row = new Array(headerRow.length).fill('');

  function set(col, val) {
    var i = headerRow.indexOf(col);
    if (i >= 0) row[i] = val;
  }

  set('Timestamp (IST)', toIST(d.timestamp));
  set('Name', d.name || '');
  set('Email', d.email || '');
  set('Tool', d.tool || '');
  set('URL', d.url || '');
  set('IP', tel.ip || '');
  set('City', tel.city || '');
  set('Country', tel.country || '');
  set('Device Type', tel.device_type || '');
  set('OS', tel.os || '');
  set('Browser', tel.browser || '');

  inputKeys.forEach(function (k) { set('in_' + k, inputs[k]); });
  resultKeys.forEach(function (k) { set('out_' + k, results[k]); });

  sheet.appendRow(row);
}

// ─── Helpers ──────────────────────────────────────────────────────────────────
function getOrCreateSheet(ss, name, headers) {
  var sheet = ss.getSheetByName(name);
  if (!sheet) {
    sheet = ss.insertSheet(name);
    var r = sheet.getRange(1, 1, 1, headers.length);
    r.setValues([headers]);
    r.setBackground('#0f172a').setFontColor('#38bdf8').setFontWeight('bold');
    sheet.setFrozenRows(1);
    sheet.setColumnWidth(1, 160);
  }
  return sheet;
}

function ensureHeaders(sheet, headers) {
  var last = sheet.getLastColumn();
  var existing = last > 0 ? sheet.getRange(1, 1, 1, last).getValues()[0] : [];
  headers.forEach(function (h) {
    if (existing.indexOf(h) === -1) {
      var col = sheet.getLastColumn() + 1;
      sheet.getRange(1, col).setValue(h)
        .setBackground('#0f172a').setFontColor('#38bdf8').setFontWeight('bold');
      existing.push(h);
    }
  });
}

function toIST(iso) {
  if (!iso) return '';
  try {
    var d = new Date(iso);
    var ist = new Date(d.getTime() + 19800000); // +5:30
    return Utilities.formatDate(ist, 'Asia/Kolkata', 'dd-MMM-yyyy HH:mm:ss');
  } catch (e) { return iso; }
}

function doGet(e) {
  return ContentService
    .createTextOutput('Quantum Step Tracker v3 — OK')
    .setMimeType(ContentService.MimeType.TEXT);
}
