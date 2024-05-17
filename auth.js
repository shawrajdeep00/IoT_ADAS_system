const express = require("express");
const router = express.Router();
require('./../db/connection');
const User = require('../model/userschema');
router.get('/', (a,b)=>{
    b.send(`hello world`);
})
router.use(express.json());
router.get("/mat", async(a,b)=>{
    try{
        const result = await User.find();
        b.send(result);
    }catch(e){
        b.send(e);
    }
});
router.get("/matl/:latn&longw", async (req,res)=>{
    try{
        const lat = req.params.latn;
        const long = req.params.longw;
        const result = await User.find({$and:[{latn:lat},{longw:long}]}).select({traffic:1, signal:1});
        if(!result){
            res.status(400).send();
        }else{
            res.send(result);
        }
    }catch(e){
        res.status(500).send(e);
    }
})

module.exports = router;