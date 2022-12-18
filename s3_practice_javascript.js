const dotenv = require("dotenv");
dotenv.config();

const AWS = require("aws-sdk");

const s3 = new AWS.S3({
    accessKeyId: process.env.AWS_ACCESS_KEY_ID,
    secretAccessKey: process.env.AWS_SECRET_ACCESS_KEY_ID,
});

const BUCKET_NAME = process.env.AWS_BUCKET_NAME || "";

// CRUD Operations

// CREATE - Create Bucket
const createBucket = (bucketName) => {
    // Create the parameters for calling createBucket
    let bucketParams = {
        Bucket: bucketName,
    };

    // call S3 to create the bucket
    s3.createBucket(bucketParams, function (err, data) {
        if (err) {
            console.log("Error", err);
        } else {
            console.log("Success", data.Location);
        }
    });
};

// READ - List buckets
const listBuckets = (s3) => {
    s3.listBuckets(function (err, data) {
        if (err) {
            console.log("Error", err);
        } else {
            console.log("Success", data.Buckets);
        }
    });
};

// CREATE - Upload files
const uploadFile = (filePath, bucketName, keyName) => {
    let fs = require("fs");
    // Read the file
    const file = fs.readFileSync(filePath);

    // Setting up S3 upload parameters
    const uploadParams = {
        Bucket: bucketName, // Bucket into which you want to upload file
        Key: keyName, // Name by which you want to save it
        Body: file, // Local file
    };

    s3.upload(uploadParams, function (err, data) {
        if (err) {
            console.log("Error", err);
        }
        if (data) {
            console.log("Upload Success", data.Location);
        }
    });
};

// READ - List files in Bucket
const listObjectsInBucket = (bucketName) => {
    // Create the parameters for calling listObjects
    let bucketParams = {
        Bucket: bucketName,
    };

    // Call S3 to obtain a list of the objects in the bucket
    s3.listObjects(bucketParams, function (err, data) {
        if (err) {
            console.log("Error", err);
        } else {
            console.log("Success", data);
        }
    });
};

// UPDATE - Update file
const renameObjectsInBucket = (bucketName, oldKeyName, newKeyName) => {
    // Create the parameters for calling listObjects
    let bucketParams = {
        Bucket: bucketName,
        CopySource: bucketName + "/" + oldKeyName,
        Key: newKeyName,
    };

    // Call S3 to rename the objects in the bucket
    s3.copyObject(bucketParams, function (err, data) {
        if (err) {
            console.log("Error", err);
        } else {
            console.log("Success", data);
        }
    });
};

// DELETE - Delete bucket
const deleteBucket = (bucketName) => {
    // Create params for S3.deleteBucket
    let bucketParams = {
        Bucket: bucketName,
    };

    // Call S3 to delete the bucket
    s3.deleteBucket(bucketParams, function (err, data) {
        if (err) {
            console.log("Error", err);
        } else {
            console.log("Success", data);
        }
    });
};

// Download file
const downloadFile = (bucketName, keyName, filePath) => {
    // Create the parameters for calling listObjects
    let bucketParams = {
        Bucket: bucketName,
        Key: keyName,
    };

    // Create the file to store the data
    const file = require("fs").createWriteStream(filePath);

    // Call S3 to retrieve the file
    s3.getObject(bucketParams)
        .createReadStream()
        .pipe(file)
        .on("error", function (err) {
            console.log("Error", err);
        })
        .on("close", function () {
            console.log("Done");
        });
};

function sleep(ms) {
    console.log("Wait...");
    return new Promise((resolve) => setTimeout(resolve, ms));
}

// Main Function to run when called
async function main() {
    console.log("\nCreating bucket : ");

    createBucket(BUCKET_NAME);
    await sleep(5000);
    console.log("\nListing out all the buckets in your AWS S3: ");

    listBuckets(s3);
    await sleep(5000);
    console.log("\nUploading image1 to " + BUCKET_NAME);

    uploadFile(
        "daniel-norin-lBhhnhndpE0-unsplash.jpg",
        BUCKET_NAME,
        "football.jpg"
    );
    await sleep(5000);

    console.log("\nUploading image2 to " + BUCKET_NAME);
    uploadFile("florian-olivo-4hbJ-eymZ1o-unsplash.jpg", BUCKET_NAME, "code.jpg");
    await sleep(5000);

    console.log(
        "\nListing out all the files/objects in the bucket " + BUCKET_NAME
    );
    listObjectsInBucket(BUCKET_NAME);
    await sleep(5000);

    console.log("\nRenaming the file in the bucket " + BUCKET_NAME);
    renameObjectsInBucket(BUCKET_NAME, "football.jpg", "football1.jpg");
    await sleep(5000);

    console.log("\nDeleting bucket : " + BUCKET_NAME);
    deleteBucket(BUCKET_NAME);

    console.log("\nDownloading file from " + BUCKET_NAME);
    downloadFile(BUCKET_NAME, "football.jpg", "football.jpg");
    await sleep(5000);
}
main();