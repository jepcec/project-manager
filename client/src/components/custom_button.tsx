interface ICustomButton{
    label: string;
    onClick: ()=>void;
}
const CustomButton = ({label,onClick}:ICustomButton) =>(
    <button onClick={onClick} className="border px-2 bg-fuchsia-300">
        {label}
    </button>
)


export default CustomButton
