const express = require("express");
const spawner = require('child_process').spawn;
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
        cb(null,file.originalname); // Set filename
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

    // Current language type
    const lang = req.body.language;
    const file = req.file;
    console.log(lang);
    console.log(file.originalname);
    // Respond with success message or do other processing
    res.send("File uploaded successfully.");


    const data = [lang,file.originalname]
    const python_process = spawner('python', ['Analyser\\main.py', JSON.stringify(data)]);
    python_process.stdout.on('data', (data) => {
        console.log(`Python Script Output: ${data}`);
      });
      python_process.stderr.on('data', (error) => {
        console.error(`Error in Python Script: ${error}`);
      });
      
      python_process.on('close', (code) => {
        console.log(`Python Script Exited with Code: ${code}`);
      });
});

const PORT = 5000;
app.listen(PORT, () => {
    console.log("server started at port " + PORT);
});
