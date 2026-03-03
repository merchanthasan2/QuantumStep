<?php
header('Access-Control-Allow-Origin: *');
header('Access-Control-Allow-Methods: POST, OPTIONS');
header('Access-Control-Allow-Headers: Content-Type');

if ($_SERVER['REQUEST_METHOD'] === 'OPTIONS') {
    exit;
}

if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $data = file_get_contents('php://input');
    $decoded = json_decode($data, true);
    
    if ($decoded) {
        $timestamp = date('Y-m-d H:i:s');
        $ip = $_SERVER['REMOTE_ADDR'];
        $os = $decoded['os'] ?? 'Unknown';
        $browser = $decoded['browser'] ?? 'Unknown';
        $location = $decoded['location'] ?? 'Unknown';
        $tool = $decoded['tool'] ?? 'Generic';
        
        $logFile = 'study_logs_' . date('Y-m-d') . '.txt';
        $logEntry = "[" . $timestamp . "] [IP: " . $ip . "] [OS: " . $os . "] [Browser: " . $browser . "] [Location: " . $location . "] [Tool: " . $tool . "]\n";
        $logEntry .= "Details: " . json_encode($decoded['details']) . "\n";
        $logEntry .= str_repeat("-", 80) . "\n";
        
        file_put_contents($logFile, $logEntry, FILE_APPEND);
        
        echo json_encode(['status' => 'success']);
    } else {
        http_response_code(400);
        echo json_encode(['status' => 'error', 'message' => 'Invalid data']);
    }
} else {
    http_response_code(405);
    echo json_encode(['status' => 'error', 'message' => 'Method not allowed']);
}
?>
