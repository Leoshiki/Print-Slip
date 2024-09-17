# Print-Slip
*Main Objective:*
  To make the process of printing slips for a dedicated delivery app more efficient, as it doesn't
contain any tool to do this automatically. This project could be useful because slips for each order
have to be written by hand, consuming a lot of effort and time.
  It needs to generate a printable document with up to three orders in an A4 sheet. 
  The slips should contain: order number, client name, full address and delivery time.

This program does the following:
- Manages the app's interface and windows
- Ensures the correct window is active before performing any action
- Captures a specific part of the screen containing the desired information and saves to an image
- Uses OCR to convert the image to text
- Adds the text into a printable document
