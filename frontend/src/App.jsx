import React from 'react'
import { useState } from 'react'
import axios from "axios"
const App = () => {
  const [userinput,setUserinput]=useState('')
  const [message,setMessage]=useState([])
  const inputHandeler=async()=>{
    console.log(userinput)
    if(!userinput.trim()) return // return nothing
    const userMessage={
      role:"user",
      text:userinput
    }
    setMessage((prev)=>[
      ...prev,userMessage
    ])
    const {data}=await axios.post("http://localhost:3000/api/ragchat",{userinput:userMessage.text})
    console.log(data)
     console.log(data.Ai)
    const AiMessage={
      role:"ai",
      text:data.Ai
    }
    setMessage((prev)=>[
      ...prev,AiMessage
    ])
    setUserinput("")
   
  }
  return (
    <div className='bg-gradient-to-t from-blue-300 to-blue-500 min-h-screen flex justify-center items-center'>
    <div className='bg-white h-[500px] w-[400px] rounded-lg shadow-2xl shadow-blue-500 overflow-hidden flex flex-col'>
     {/*  chat header */}
      <div className='bg-blue-500 text-xs text-center text-white p-1 py-2'><h1>CLIMATE<br/>RAGCHATBOT</h1></div>
      {/* 
      chatbody */}
      <div className='flex-1 overflow-y-auto space-y-3 bg-blue-200  px-2 '>

{
  message.map((msg,index)=>(
    <div key={index} className={` mt-2 max-w-[80%] shadow px-4 rounded-lg py-2 text-xs ${msg.role==="user"?"mr-auto bg-blue-500 text-white":"bg-white text-black ml-auto"}`}>
      {msg.text}
    </div>
  ))
}
      </div>
      {/* inputbody */}
      <div className='flex gap-2 px-2 bg-blue-200 p-3'>
<input type="text"
onChange={(e)=>setUserinput(e.target.value)}
value={userinput}
 placeholder='Type your message' 
 className='bg-white w-full  rounded-lg py-3 px-4 placeholder:text-gray-400 placeholder:text-center focus:ring-2 focus:ring-blue-300 outline-none' />
      <button onClick={inputHandeler} className='font-bold text-white bg-blue-500 px-4 rounded-md py-3'>send</button>
      </div>
    </div>
    </div>
  )
}

export default App
