<?php
$received_data = strval($_POST["image"]); // Get the submitted image data.
$processed_data = json_decode($received_data, true); // Decode the JSON data received.

//print_r($processed_data);

if ($processed_data["identifier"] == "g7!#73gb") {
    $image_data = base64_decode($processed_data["image"]); // Decode the image from the received data.
    file_put_contents("/dev/shm/oracle.jpg", $image_data);
    echo "Success";
} else {
    echo "Permission denied";
}
?>
