<?php
header('Access-Control-Allow-Origin: *');
header('Access-Control-Allow-Methods: POST, OPTIONS');
header('Access-Control-Allow-Headers: Content-Type');

if ($_SERVER['REQUEST_METHOD'] === 'OPTIONS') {
    http_response_code(200);
    exit;
}

if ($_SERVER['REQUEST_METHOD'] !== 'POST') {
    http_response_code(405);
    echo json_encode(['error' => 'Method Not Allowed']);
    exit;
}

// 1. Validate Upload Directory
$uploadDir = __DIR__ . '/uploads/';
if (!file_exists($uploadDir)) {
    mkdir($uploadDir, 0755, true);
}

// 2. Process Uploaded File
if (!isset($_FILES['logo']) || $_FILES['logo']['error'] !== UPLOAD_ERR_OK) {
    http_response_code(400);
    echo json_encode(['error' => 'No file uploaded or upload error occurred. ' . $_FILES['logo']['error']]);
    exit;
}

$file = $_FILES['logo'];

// 3. Security: Validate File Type
$allowedMimeTypes = ['image/jpeg', 'image/png', 'image/gif', 'image/svg+xml'];
$finfo = finfo_open(FILEINFO_MIME_TYPE);
$mimeType = finfo_file($finfo, $file['tmp_name']);
finfo_close($finfo);

if (!in_array($mimeType, $allowedMimeTypes)) {
    http_response_code(400);
    echo json_encode(['error' => 'Invalid file type. Only JPG, PNG, GIF, and SVG are allowed.']);
    exit;
}

// 4. Security: Limit File Size (5MB)
if ($file['size'] > 5 * 1024 * 1024) {
    http_response_code(400);
    echo json_encode(['error' => 'File size exceeds the 5MB limit.']);
    exit;
}

// 5. Generate Safe Filename
$extension = pathinfo($file['name'], PATHINFO_EXTENSION);
if (empty($extension)) {
    // Fallback extension based on mime type
    $extMap = [
        'image/jpeg' => 'jpg',
        'image/png' => 'png',
        'image/gif' => 'gif',
        'image/svg+xml' => 'svg'
    ];
    $extension = $extMap[$mimeType];
}
$safeFilename = time() . '_' . bin2hex(random_bytes(8)) . '.' . $extension;
$destination = $uploadDir . $safeFilename;

// 6. Move File
if (move_uploaded_file($file['tmp_name'], $destination)) {
    // Get the base URL securely depending on server context
    $protocol = isset($_SERVER['HTTPS']) && $_SERVER['HTTPS'] === 'on' ? "https" : "http";
    $host = $_SERVER['HTTP_HOST'];
    $path = rtrim(dirname($_SERVER['PHP_SELF']), '/\\');
    
    $fileUrl = $protocol . "://" . $host . $path . "/uploads/" . $safeFilename;
    
    echo json_encode([
        'success' => true,
        'url' => $fileUrl,
        'message' => 'File uploaded successfully'
    ]);
} else {
    http_response_code(500);
    echo json_encode(['error' => 'Failed to move uploaded file.']);
}
?>
