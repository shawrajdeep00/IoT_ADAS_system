const mongoose = require("mongoose");

const uri = process.env.DATABASE;

mongoose.connect(uri,{
    useNewUrlParser: true,
    useUnifiedTopology: true,
}).then(()=>{
    console.log(`connection success`);
}).catch((err)=>console.log(err));
