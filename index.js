const express = require("express");
const multer = require("multer");
const cors = require("cors");

const app = express();

app.use(cors());
app.use(express.static("./uploads"));

const storage = multer.diskStorage({
    destination: (req, file, cb) => {
        cb(null, "./uploads"); // Set your upload directory
    },
    filename: (req, file, cb) => {
        cb(null, file.originalname); // Set filename
    }
});

let upload = multer({
    storage: storage
}).single("file");

// Route to handle file upload
app.post("/upload", upload, (req, res) => {
    if (!req.file) {
        return res.status(400).send("No files were uploaded.");
    }

    // Access the file using req.file
    console.log(req.file);

    // Respond with success message or do other processing
    res.send("File uploaded successfully.");
});

const PORT = 5000;
app.listen(PORT, () => {
    console.log("server started at port " + PORT);
});
