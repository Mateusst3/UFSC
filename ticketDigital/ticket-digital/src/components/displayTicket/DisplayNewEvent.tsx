export default function DisplayNewEvent(props: {
  image: string;
  name: string;
  category: string;
}) {
  return (
    <>
      <section className="w-auto h-auto flex flex-col py-6 px-5 rounded gap-4 bg-[#181818]">
        <img src={props.image} alt="" className="rounded" />
        <p className="text-center w-full text-white text-lg">{props.name}</p>
        <p className="text-start text-[#B3B3B3] text-sm">{props.category}</p>
      </section>
    </>
  );
}
