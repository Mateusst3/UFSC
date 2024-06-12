import { motion } from "framer-motion";
import { useRouter } from "next/router";
import { useState } from "react";
import { AiFillHome } from "react-icons/ai";
import {
  FaRegArrowAltCircleLeft,
  FaRegArrowAltCircleRight,
  FaUserFriends,
} from "react-icons/fa";
import { FaMagnifyingGlass, FaRankingStar, FaWallet } from "react-icons/fa6";
import { IoTicketSharp } from "react-icons/io5";
import { MdStars } from "react-icons/md";

export default function SideMenu() {
  const [isOpen, setIsOpen] = useState<boolean>(false);
  const router = useRouter();
  return (
    <>
      <motion.section
        initial={{ x: -100 }}
        animate={{ x: 0 }}
        transition={{ ease: "easeOut", duration: 2 }}
        className={`absolute z-50 top-0 left-0 md:relative ${
          isOpen ? "flex" : "hidden"
        } flex-col py-12 gap-6 px-3 w-auto h-auto bg-black`}
      >
        <button
          className={`absolute p-3 bg-gray-700 rounded-full -right-5 top-2`}
          onClick={() => setIsOpen(false)}
        >
          <FaRegArrowAltCircleLeft className="text-white" />
        </button>
        <div className="w-full flex flex-row justify-center items-center">
          <img src="/images/Logo.png" alt="" className="w-[180px]" />
        </div>
        <div className="w-full flex flex-row justify-center items-center">
          <img src="/images/name.png" alt="" className="w-[258px]" />
        </div>
        <section className="flex flex-col px-3">
          <button
            className="w-[300px] flex flex-row items-center gap-6 justify-start h-auto px-6 py-4 text-white bg-black hover:bg-[#587295] transition rounded-lg"
            onClick={() => router.push("/")}
          >
            <AiFillHome className="text-4xl" />
            <p className="text-white text-xl font-bold">Início</p>
          </button>
          <button
            className="w-[300px] flex flex-row items-center gap-6 justify-start h-auto px-6 py-4 text-white bg-black hover:bg-[#587295] transition rounded-lg"
            onClick={() => router.push("/buscar")}
          >
            <FaMagnifyingGlass className="text-4xl" />
            <p className="text-white text-xl font-bold">Busca</p>
          </button>
          <button className="w-[300px] flex flex-row items-center gap-6 justify-start h-auto px-6 py-4 text-white bg-black hover:bg-[#587295] transition rounded-lg"
            onClick={() => router.push("/tickets")}
          >
            <IoTicketSharp className="text-4xl" />
            <p className="text-white text-xl font-bold">Seus Tickets</p>
          </button>
          <button className="w-[300px] flex flex-row items-center gap-6 justify-start h-auto px-6 py-4 text-white bg-black hover:bg-[#587295] transition rounded-lg">
            <MdStars className="text-4xl" />
            <p className="text-white text-xl font-bold">Pontuação</p>
          </button>
          <button className="w-[300px] flex flex-row items-center gap-6 justify-start h-auto px-6 py-4 text-white bg-black hover:bg-[#587295] transition rounded-lg">
            <FaWallet className="text-4xl" />
            <p className="text-white text-xl font-bold">Carteira</p>
          </button>
          <button className="w-[300px] flex flex-row items-center gap-6 justify-start h-auto px-6 py-4 text-white bg-black hover:bg-[#587295] transition rounded-lg">
            <FaUserFriends className="text-4xl" />
            <p className="text-white text-xl font-bold">Amigos</p>
          </button>
          <button className="w-[300px] flex flex-row items-center gap-6 justify-start h-auto px-6 py-4 text-white bg-black hover:bg-[#587295] transition rounded-lg">
            <FaRankingStar className="text-4xl" />
            <p className="text-white text-xl font-bold">Classificação</p>
          </button>
        </section>
      </motion.section>
      {!isOpen && (
        <button
          className={`absolute p-3 bg-gray-700 rounded-full ${isOpen} -left-3 top-2`}
          onClick={() => setIsOpen(true)}
        >
          <FaRegArrowAltCircleRight className="text-white" />
        </button>
      )}
    </>
  );
}
