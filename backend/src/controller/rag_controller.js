import { Rag_prompt } from "../spawn.js"

export const rag_controller=async(req,res)=>{
  try {
      const{userdata}=req.body
      
  const Ai_result=await Rag_prompt(userdata)
console.log(Ai_result)
  res.status(200).json({
success:true,
message:"Ai data fectched successfully",
Ai:Ai_result
  
  })
  } catch (error) {
    res.status(500).json({
      success:false,
      message:"error in the ai fectching data",
      error:error
    })
  }

  
} 