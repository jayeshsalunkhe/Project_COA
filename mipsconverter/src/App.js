import Form from "./form";
import { useState, useEffect } from "react";
import "antd/dist/antd.css";
import { Upload } from "antd";
import { UploadOutlined } from "@ant-design/icons";
import "./App.css";
import axios from "axios";
import backgroundVideo from "./background_video.mov";
import { Button } from "antd";
const BACKEND_URL = "http://127.0.0.1:5000/";
// import Form from './form'

function App() {
  const handleAssemble = async () => {
    console.log({ data: assembleText });
    const senddata = { data: assembleText };
    await axios.post("http://127.0.0.1:5000/assemble", senddata).then((res) => {
      console.log(res.data.data);
      setDisassembleText(res.data.data);
    });
  };
  const handleDisassemble = async () => {
    console.log({ data: disassembleText });
    const senddata = { data: disassembleText };
    await axios
      .post("http://127.0.0.1:5000/disassemble", senddata)
      .then((res) => {
        console.log(res.data.data);
        setAssembleText(res.data.data);
      });
  };
  const [assembleText, setAssembleText] = useState("");
  const [disassembleText, setDisassembleText] = useState("");

  return (
    <>
      <video
        className="videoTag"
        autoPlay
        loop
        muted
        style={{ position: "fixed", width: "100%", zIndex: -1, margin: "0px" }}
      >
        <source src={backgroundVideo} type="video/mp4" />
      </video>
      <div style={{ display: "grid", placeItems: "center" }}>
        <div>
          <br />
          <div>
            <div style={{ display: "flex", alignItems: "center" }}>
              <img
                src="https://upload.wikimedia.org/wikipedia/en/thumb/a/a2/IIT_Gandhinagar_Logo.svg/220px-IIT_Gandhinagar_Logo.svg.png"
                alt="IITGn Logo"
                style={{
                  height: "100px",
                  backgroundColor: "rgba(255,255,255,0.01)",
                  borderRadius: "100%",
                }}
              />
              &nbsp;
              <h1
                style={{
                  fontSize: "50px",
                  color: "#89cff0",
                  margin: "auto",
                  textShadow: "2px 2px black",
                  fontFamily: "Merriweather, serif",
                }}
              >
                MIPS Assemble/Disassemble
              </h1>
            </div>
          </div>
          <div style={{ display: "grid", placeItems: "center" }}>
            <div style={{ display: "flex", alignItems: "center" }}>
              <div
                style={{
                  display: "grid",
                  placeItems: "center",
                  padding: "20px",
                }}
              >
                <textarea
                  autoFocus
                  type="text-area"
                  style={{
                    minHeight: "70vh",
                    width: "300px",
                    padding: "10px",
                  }}
                  value={assembleText}
                  onChange={(e) => {
                    setAssembleText(e.target.value);
                  }}
                ></textarea>
                <br />
                <div>
                  <Button
                    type="primary"
                    onClick={handleAssemble}
                    style={{
                      backgroundColor: "#00ffef",
                      borderRadius: "10px",
                      fontSize: "20px",
                      fontFamily: "Merriweather, serif",
                      color: "black",
                      margin: "10px",
                      height: "50px",
                    }}
                  >
                    Assemmble
                  </Button>
                  <Upload
                    accept=".txt, .csv"
                    showUploadList={false}
                    beforeUpload={(file) => {
                      const reader = new FileReader();

                      reader.onload = (e) => {
                        console.log(e.target.result);
                        setAssembleText(e.target.result);
                      };
                      reader.readAsText(file);
                      return false;
                    }}
                  >
                    <Button
                      type="primary"
                      style={{
                        backgroundColor: "#00ffef",
                        borderRadius: "10px",
                        fontSize: "20px",
                        fontFamily: "Merriweather, serif",
                        color: "black",
                        margin: "10px",
                        height: "50px",
                      }}
                    >
                      <UploadOutlined type="upload" />
                    </Button>
                  </Upload>
                </div>
              </div>
              &nbsp;
              <div
                style={{
                  display: "grid",
                  placeItems: "center",
                  padding: "20px",
                }}
              >
                <textarea
                  type="text-area"
                  style={{
                    minHeight: "70vh",
                    
                    width: "600px",
                    padding: "10px",
                  }}
                  value={disassembleText}
                  onChange={(e) => {
                    setDisassembleText(e.target.value);
                  }}
                ></textarea>
                <br />

                <div>
                  <Button
                    type="primary"
                    onClick={handleDisassemble}
                    style={{
                      backgroundColor: "#00ffef",
                      fontSize: "20px",
                      borderRadius: "10px",
                      fontFamily: "Merriweather, serif",
                      color: "black",
                      margin: "auto",
                      height: "50px",
                    }}
                  >
                    Disassemmble
                  </Button>
                  <Upload
                    accept=".txt, .csv"
                    showUploadList={false}
                    beforeUpload={(file) => {
                      const reader = new FileReader();
                      reader.onload = (e) => {
                        console.log(e.target.result);
                        setAssembleText(e.target.result);
                      };
                      reader.readAsText(file);

                      // Prevent upload
                      return false;
                    }}
                  >
                    <Button
                      type="primary"
                      style={{
                        backgroundColor: "#00ffef",
                        borderRadius: "10px",
                        fontSize: "20px",
                        fontFamily: "Merriweather, serif",
                        color: "black",
                        margin: "10px",
                        height: "50px",
                      }}
                    >
                      <UploadOutlined type="upload" />
                    </Button>
                  </Upload>
                </div>
              </div>
            </div>
          </div>
        </div>

        {/* <Form/> */}
      </div>
    </>
  );
}

export default App;
