const express = require("express");
const mongoose = require("mongoose");
const dotenv = require("dotenv");
const app = express();

dotenv.config({path:'./config.env'});
const port = process.env.PORT ; 
const matrix = require('./db/connection');
app.use(require('./router/auth'));
//const user=

app.get('/', (a,b)=>{
    b.send(`hello`);
})

app.listen(port, function () {
    console.log(`server started at ${port}`);
});