<?php
$received_data = strval($_POST["image"]); // Get the submitted image data.
$processed_data = json_decode($received_data, true); // Decode the JSON data received.

$image_data = base64_decode($processed_data["image"]); // Decode the image from the received data.
file_put_contents("./test.jpg", $image_data);
?>
