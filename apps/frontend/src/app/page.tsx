"use client";
import { useState } from "react";

const UploadFile = () => {
  const [file, setFile] = useState<File | null>(null)

  const handleChange = (e: any) => {
    setFile(e.target.files[0]);
  };

  const handleSubmit = async (e: any) => {
    e.preventDefault();

    const formData = new FormData();
    formData.append("file", file as File);

    try {
      const response = await fetch("https://turbo-space-goggles-qxgjx945gw626gx-8000.app.github.dev/api/predict", {
        method: "POST",
        body: formData,
      });
      if (response.status === 200) {
        const result = await response.json();
        console.log("result", result);
      } else {
        console.error("Upload failed.");
      }
    } catch (error: any) {
      console.error(error);
    }
  };

  return (
    <form onSubmit={handleSubmit} method="POST">
      <input type="file" onChange={handleChange} />
      <button type="submit">Upload</button>
    </form>
  );
};

export default UploadFile;