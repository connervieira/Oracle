<?php
include "./config.php"

$received_data = strval($_POST["image"]); // Get the submitted image data.
$processed_data = json_decode($received_data, true); // Decode the JSON data received.

if (in_array($processed_data["identifier"], config["auth"]["permitted_devices"])) {
    $image_data = base64_decode($processed_data["image"]); // Decode the image from the received data.
    file_put_contents("./test.jpg", $image_data);
    echo "Success";
} else {
    echo "Permission denied";
}
?>
