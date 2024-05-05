const express = require("express");
const routes = require("./routes/start");
const cors = require("cors");
const app = express();
const port = 3000;
const ip = require("ip");
const ipAddr = ip.address();


app.use(cors());
app.use(express.json());
app.use("/", routes);
app.get("/", (req, res) => {
  res.json({ house: lastHouseVisited });
});
app.post("/", (req, res) => {
  lastHouseVisited = req.body.house;
  res.json({ house: lastHouseVisited });
});

app.listen(port, () => {
  console.log("Server run : http://" + ipAddr + ":" + port);
});
