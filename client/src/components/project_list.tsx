import { useState } from "react"

type TextItem ={
    id: number;
    text: string;
}
function ProjectList()
{
    const [items, setItems] = useState([
    { id: 1, text: "Tarea 1: Terminar el login" },
    { id: 2, text: "Tarea 2: Conectar API" },
    { id: 3, text: "Reunión con equipo a las 3 PM" },
    { id: 4, text: "Deploy a producción" },
    ]);
    const addItem = ()=>{
        setItems([...items]);
    }

    const click_item_project = ()=>{
        console.log("Presionando btn")
    }
    return(
        <div>
            <h1>Proyectos</h1>
            <div>
                {items.map((item, index)=> (
                    <div key={index} onClick={click_item_project} className="cursor-pointer active:bg-gray-300 hover:bg-gray-200">
                        <span>{item.text}</span>
                    </div>
                ))}
            </div>
        </div>
    )
}

export default ProjectList