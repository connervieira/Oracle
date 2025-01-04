<?php
$image_data = base64_encode(file_get_contents("/dev/shm/oracle.jpg"));

?>
<!DOCTYPE html>
<html>
    <head>
        <title>Oracle</title>
        <meta http-equiv="refresh" content="10" />
    </head>
    <body>
        <img style="width:100%;" src="data:image/jpg;base64,<?php echo $image_data; ?>">
    </body>
</html>
