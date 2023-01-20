# ManipulatorWithCameraProject
This is a project of control programme of manipulator with camera to scan QR codes on arriving packages.

This programme is written in python language and it's controlling Raspberry PI GPIOs. To the Raspberry Pi are connected servos and camera. When the package arrives at the position it crosses the infrared beam and it's the signal for the system to start scanning QR code. When the camera is unable to find the QR within 5 seconds, code the manipulator moves it to scan it on another surface.
