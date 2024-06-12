import { AiFillHome } from "react-icons/ai";

export default function DisplayTicketHome(props: {
  image: string;
  name: string;
}) {
  return (
    <div className="flex flex-row items-start justify-start h-auto w-[300px] bg-[#303030] rounded-md">
      <img src={props.image} alt="" />
      <section className="flex flex-row items-center justify-center h-full w-full p-3">
        <p className="text-white font-bold text-lg">{props.name}</p>
      </section>
    </div>
  );
}
