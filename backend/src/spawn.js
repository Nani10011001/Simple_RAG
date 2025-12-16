import { rejects } from "assert"
import {spawn} from "child_process"

import path from "path"
import { fileURLToPath } from "url"

const __filepath=fileURLToPath(import.meta.url)
const __dirname=path.dirname(__filepath)
const pythonFile=path.resolve(__dirname,"RagAgent","main.py")

const pythonAgent=spawn('python',[pythonFile])


pythonAgent.stderr.on('data',(err)=>{
    console.log("err of stderr: ",err.toString())
})
pythonAgent.on('close',(code)=>{
    console.log(`proccess code exit: ${code}`)
})
export const Rag_prompt=(prompt)=>{

    return new Promise((resolve,rejects)=>{
        
            pythonAgent.stdout.once("data",(data)=>{
                try{
                    const parse=JSON.parse(data.toString())

              resolve(parse.output)  
       


                }catch(error){
rejects("error in the output display of it")
  
           console.log(error) 
                }
             
            })
         
      
    
        pythonAgent.stdin.write(JSON.stringify({input:prompt})+"\n")
    })

}