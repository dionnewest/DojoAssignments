const express = require("express");
const bodyParser = require("body-parser");
const app = express();

//middleware
app.use(bodyParser.json())
//app.use(bodyParser.urlencoded())


//mongoose file

//routes

app.listen(port, () => console.log(`listening on port ${port}`))