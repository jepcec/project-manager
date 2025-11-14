import CustomButton from "./custom_button"
import ProjectConfig from "./project_config"
import ProjectTask from "./project_task"
import { useState } from "react"
function Project(){
    const [ventanaActiva, setVentanaActiva] = useState("configuracion")
    let ventana
    if(ventanaActiva === "configuracion")
        ventana = <ProjectConfig/>
    else{
        ventana = <ProjectTask/>
    }
    return (
        <div className="bg-blue-300">
            <div className="flex flex-row p-2 space-x-2">
            <CustomButton label="name-project" onClick={()=>{setVentanaActiva("configuracion")}}/>
            <CustomButton label="tarea" onClick={()=>{setVentanaActiva("tareas")}}/>
            </div>

            <div>
                {ventana}
            </div>
        </div>
    )
}
export default Project