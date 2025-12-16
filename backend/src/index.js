import express from "express"
import cors from "cors"
import dotenv from "dotenv"
import RagAgent from "./router/rag.router.js"
dotenv.config()
const app=express()
app.use(cors())
app.use(express.json())

//rag router
app.use('/api',RagAgent)


//app listen port

app.listen(process.env.PORT,console.log(`server running at http://localhost:${process.env.PORT}`))