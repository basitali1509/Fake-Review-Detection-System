import { Button, Typography } from "@material-tailwind/react";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faAngleDoubleRight, faCheckDouble } from "@fortawesome/free-solid-svg-icons";
import { useEffect } from "react";
import AOS from 'aos';
import 'aos/dist/aos.css';
import { Link } from 'react-router-dom';
import NavBar from "../Components/NavBar";
import Footer from "../Components/Footer";
import { Routes,Route } from 'react-router-dom';
import Surveillance from "../Assets/1710586854274-removebg-preview.png";
import AboutPage from "./About";
import SignInPage from "./SignIn";
import { SignInModal } from "../Components/ModalSignin copy";

const HomePage = () => {
    useEffect(() => {
        AOS.init({
            duration: 1000, // Change the animation duration as per your preference
            once: true, // Set to true if you want the animation to occur only once
        });
    }, []);

    return (
        <div className="text-white">
            <div className="min-h-screen flex flex-col">
                <NavBar />
                <div className="flex-grow flex flex-col  lg:flex-row justify-center">
                    <div className="flex-1 flex flex-col gap-8 lg:gap-10 px-8 lg:px-12 py-16 lg:py-36 text-justify lg:text-left transition-all duration-400">
                        <div className="flex flex-col gap-10 lg:gap-12">
                            <Typography
                                variant="h1"
                                className="text-center lg:text-left text-3xl lg:text-4xl 2xl:text-6xl transition-all duration-400"
                                style={{ textShadow: "0px 1px 2px rgba(255, 255, 255, 0.5)" }}
                                data-aos="fade-right"
                            >
                                Track <span className="text-green-500">Positive</span>, <span className="text-red-700">Negative</span>{" "}
                                <span className="text-[#3ae3a6]">Real & Fake</span>
                            </Typography>
                            <Typography data-aos="fade-left">
                                Sentiment Analysis is a process of computationally identifying and categorizing opinions expressed in a piece of text, determining whether the sentiment expressed is positive, negative, or neutral. It's widely used in understanding customer feedback, social media monitoring, and market research. A Fake Review Model and System employs advanced algorithms to detect and filter out fraudulent reviews from genuine ones.
                            </Typography>
                        </div>
                      
                        <div className="flex justify-center lg:justify-start">

                            <SignInModal/>

                        </div>
                    </div>
                    <div className="flex-1 flex items-center justify-center">
                        <img
                            src={Surveillance}
                            alt=""
                            className="w-[28rem] max-w-3xl p-8 md:p-4 lg:p-0 transition-all duration-400"
                            // style={{ filter: "drop-shadow(0px 4px 4px rgba(255, 255, 255, 0.5))" }}
                            data-aos="fade-up"
                        />
                    </div>
                </div>
                <AboutPage />
            </div>
            <Footer />
        </div>
    );
};

export default HomePage;
