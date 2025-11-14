import CustomButton from "../components/custom_button"
import ProjectList from "../components/project_list"

import Project from "../components/project"
function Home()
{
    return(
        <div className="flex h-screen border">
            <aside className="w-1/5 border-r p-4 bg-emerald-300">
                <CustomButton label="new project +" onClick={()=> console.log("Mi funcion")}/>
                <ProjectList/>
            </aside>
            <main className="flex-1 p-4 bg-green-400">
                <Project/>
            </main>
        </div>
    )
}


export default Home