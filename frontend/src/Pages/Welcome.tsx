import { Link } from "react-router-dom";
import AnimatedWrapper from "../Components/Layout/AnimatedWrapper";

const Welcome = () => {
    return (
        <AnimatedWrapper>
            <div>
                Welcome to your tasks Dashboard. Next you can proceed to the
                list of <Link to="/todos/all">tasks</Link>
            </div>
        </AnimatedWrapper>
    );
};

export default Welcome;
