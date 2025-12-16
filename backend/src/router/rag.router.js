import express from 'express'
import { rag_controller } from '../controller/rag_controller.js'
const RagAgent=express.Router()
RagAgent.post('/ragchat',rag_controller)
export default RagAgent