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
    return(
        <div>
            <h1>Proyectos</h1>
            <div>
                {items.map((item)=> (
                    <div>
                        <span>{item.text}</span>
                    </div>
                ))}
            </div>
        </div>
    )
}

export default ProjectList