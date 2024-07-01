import React, { useEffect } from "react";

const Checkout = () => {
    const BACKEND_URL = import.meta.env.VITE_APP_BACKEND_URL;

    useEffect(() => {
        console.log("BACKEND_URL == ", BACKEND_URL);
    }, [BACKEND_URL]);

    return (
        <div className="container">
            <h1>Checkout</h1>
            <a href="https://alexanderpershin.github.io/portfolio/#/">
                Alexander
            </a>
            <h2>Price</h2>
            <h3>25$</h3>
            <form
                action={`${BACKEND_URL}/checkout/create-checkout-session/`}
                method="POST"
            >
                <input type="hidden" name="product_name" value="test_product" />
                <input type="hidden" name="price" value={25 * 100} />
                <button className="btn-checkout" type="submit">
                    Checkout
                </button>
            </form>
        </div>
    );
};

export default Checkout;
