import CustomButton from "./custom_button"
import { useState} from "react"
function ProjectConfig(){
    const [nombre, setNombre] = useState("")
    const [descripcion, setDescripcion] = useState("")

    return (
        <div className="bg-amber-200 border p-2">
            <form className="flex flex-col">
                <div>
                    <label htmlFor="nombre">nombre</label>
                    <input type="text" />
                </div>

                <div> 
                    <label htmlFor="descripcion">descripcion</label>
                    <input type="text" />
                </div> 
                <div>
                    <CustomButton label="Gurdar" onClick={()=>{}}/> 
                    <CustomButton label="Cancelar" onClick={()=>{}}/>
                </div>
            </form>
        </div>
    )
}

export default ProjectConfig