# Oracle
A simple image streaming system for web-cameras behind a firewall.

## Note

This is a system I developed quickly for a personal project. It has not been proofread, bug tested, or otherwise audited. It is entirely possible that there are glaring security vulnerabilities. Please use extreme caution when implementing Oracle into your own projects.

## Description

Oracle is a simple streaming system that works in the opposite way most webcam streams work. Instead of streaming images from a server to a client viewing it, Oracle streams images from a client to a central server. This makes it possible to stream webcam images from any network device that has access to the internet, without needing any network configuration on the camera side. Oracle should be able to stream images, even if the webcam is behind a firewall, and has not been port-forwarded.

## Components

This project consists of two components. The "sender" is the device that captures images and sends them to a server. The "receiver" is the server that processes images from the sender, so they can be viewed by clients.
