import { FC, ReactNode } from "react";
import { motion } from "framer-motion";

interface AnimatedWrapperProps {
    children: ReactNode;
}

const AnimatedWrapper: FC<AnimatedWrapperProps> = ({ children }) => {
    const variants = {
        hidden: { opacity: 0, x: -1000, y: 0 },
        enter: { opacity: 1, x: 0, y: 0 },
        exit: { opacity: 0, x: 1000, y: 0 },
    };

    return (
        <motion.div
            initial="hidden"
            animate="enter"
            exit="exit"
            variants={variants}
            transition={{ duration: 0.2, type: "easeInOut" }}
            className="relative"
        >
            {children}
        </motion.div>
    );
};

export default AnimatedWrapper;
