// eslint-disable-next-line no-unused-vars
import React, { useState, useEffect } from 'react';
import { useSelector } from 'react-redux';

const SuperCoin = () => {
  const [superCoins, setSuperCoins] = useState(0);

  const cartItems = useSelector((state) => state.cart.items);

  const totalAmount = cartItems.reduce((total, item) => total + item.price * item.quantity, 0);

  useEffect(() => {
    if (totalAmount >= 100 && totalAmount < 200) {
      setSuperCoins(10);
    } else if (totalAmount >= 200 && totalAmount < 300) {
      setSuperCoins(20);
    } else if (totalAmount >= 300) {
      setSuperCoins(30);
    } else {
      setSuperCoins(0);
    }
  }, [totalAmount]);

  return (
    <div>
      You have earned {superCoins} Super Coins
    </div>
  );
};

export default SuperCoin;