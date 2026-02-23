# Implementation Plan - Home Loan Calculator (Quantum Step)

This plan outlines the development of a comprehensive Home Loan Calculator with Amortization Schedule, Prepayments, and Visualizations, matching the existing "Quantum Step" design aesthetics.

## User Objectives
- **Calculate Home Loan Metrics**: EMI, Total Interest, Total Payment.
- **Detailed Amortization**: Month-by-month breakdown.
- **Prepayment Handling**: Allow monthly prepayments with options to **Reduce Tenure** or **Reduce EMI**.
- **Visuals**: Charts (Pie/Bar) and specific breakdown cards.
- **Export**: PDF/CSV options.

## Technology Stack
- **Core**: HTML5, Vanilla JavaScript (State-Based Architecture).
- **Styling**: Tailwind CSS (matching existing theme).
- **Libraries**: 
    - `Chart.js` (for visualizations).
    - `jspdf` & `jspdf-autotable` (for PDF export).

---

## Phase 1: Core Layout & Basic Calculations
**Goal**: Create the file structure and ensure basic EMI calculation works.

1.  **File Creation**: Create `tool-home-loan-calculator.html`.
2.  **UI Scaffold**: 
    - Copy Header/Nav from `index.html` / `tool-salary-calculator.html`.
    - Create a 2-Column Layout (Inputs Left, Summary Right).
3.  **Input Section**:
    - **Home Value** (Input)
    - **Down Payment** (Slider + Input, %) - Auto-calculates Loan Amount.
    - **Interest Rate** (Input).
    - **Tenure** (Dropdown: 5-30 years + Custom Input).
    - **Extras**: Agent Commission, Reg Fees.
4.  **Core Logic**:
    - Implement `calculateEMI(principal, rate, tenure)` function.
    - Calculate `Total Interest`, `Total Amount`, `LTV`.
5.  **Summary Card**: Display Monthly EMI, Total Interest, and Total Payable.

## Phase 2: Amortization Engine & Prepayment Logic
**Goal**: Generate the schedule and handle the complex prepayment math.

1.  **Amortization Function**: 
    - Create `generateSchedule(principal, rate, tenure, prepayments)` returning an array of months.
    - Loop month-by-month:
        - Calculate Interest for month.
        - Calculate Principal component (`EMI - Interest`).
        - Deduct Prepayment (if any) from Balance.
2.  **Prepayment Handling (The "One-Time Choice")**:
    - **Option A (Reduce Tenure)**: Keep EMI constant. If prepayment happens, balance reduces faster, loop ends earlier.
    - **Option B (Reduce EMI)**: Recalculate EMI based on new balance and *remaining* tenure.
3.  **Data Structure**: Maintain a `prepayments` object mapping `monthIndex -> amount`.

## Phase 3: Interactive Amortization UI
**Goal**: Display the table and allow user interaction.

1.  **Table Rendering**:
    - Columns: Month, EMI, Principal, Interest, **Prepayment (Input)**, Balance.
    - Use Virtual Scrolling or Pagination if 30 years (360 rows) is too heavy, or just render all (modern browsers handle 360 rows fine).
2.  **Interaction**:
    - Add Input field in "Prepayment" column.
    - On change: Update `prepayments` state -> Re-run `generateSchedule` -> Re-render Table & Summary.
3.  **Impact Analysis**:
    - Show "Money Saved" or "Time Saved" based on the selected Prepayment Strategy.

## Phase 4: Visualizations
**Goal**: Add charts for better insights.

1.  **Pie Chart**: Principal vs Interest Breakup.
2.  **Bar Chart**: Yearly Balance Reduction or Interest vs Principal over years.
3.  **Integration**: Use `Chart.js`, creating canvas elements in the "Summary" section. Update charts on every calculation.

## Phase 5: Export & Polish
**Goal**: Final features and design capability.

1.  **Export**:
    - **CSV**: Generate a comma-separated string and trigger download.
    - **PDF**: Use `jspdf` to render the Summary and Amortization Table.
2.  **Responsiveness**: Ensure tables scroll horizontally on mobile, inputs stack correctly.
3.  **Validation**: Prevent negative numbers, handle 0 interest, etc.

---

## Task List

### Stage 1: Scaffold & Basic Math
- [ ] Create `tool-home-loan-calculator.html` with Nav/Header.
- [ ] Implement Input Form (Home Value, Down Payment, Rate, Tenure).
- [ ] Implement `calculateEMI` logic.
- [ ] detailed Summary Card (EMI, Interest, Upfront Costs).

### Stage 2: Amortization Logic & UI
- [ ] Develop `generateAmortizationSchedule` function.
- [ ] Implement support for **Prepayment Inputs** in the logic.
- [ ] Implement **Reduce Tenure** vs **Reduce EMI** toggles.
- [ ] Render HTML Table for the schedule.

### Stage 3: Charts & Exports
- [ ] Integrate `Chart.js` for Principal/Interest Pie Chart.
- [ ] Add "Export to CSV" functionality.
- [ ] Add "Export to PDF" functionality.
- [ ] Final UI Polish (Glassmorphism adjustments).
