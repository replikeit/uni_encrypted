// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "../interfaces/IUniswapV3Pool.sol";
import "../interfaces/IERC20.sol";
import "../interfaces/IUniswapV3SwapCallback.sol";


contract UniEncrypted is IUniswapV3SwapCallback {

    uint160 internal constant MIN_SQRT_RATIO = 4295128739 + 1;
    uint160 internal constant MAX_SQRT_RATIO = 1461446703485210103287273052203988822378723970342 - 1;

    address weth;
    
    constructor(address weth_) {
        weth = weth_;
    }

    function encodedSwap(bytes memory inputData) public {
        (address pool_address, uint256 amount) = decryptInput(inputData);

        IUniswapV3Pool pool = IUniswapV3Pool(pool_address);

        require(pool.token0() == weth || pool.token1() == weth, "error: Pool have not WETH token");

        bool zeroForOne = pool.token0() == weth;
        pool.swap(
            msg.sender, 
            zeroForOne,
            int256(amount), 
            zeroForOne ? MIN_SQRT_RATIO : MAX_SQRT_RATIO,
            "0x");
    }

    function decryptInput(bytes memory inputData) private pure returns(address, uint256) {
        uint256 key_length = inputData.length >> 1;

        uint160 address_int = 0;
        for (uint8 i = 0; i < 20; ++i){
            address_int = (address_int << 8) + uint8(inputData[i] ^ inputData[key_length + i]);
        }

        uint256 amount = 0;
        for (uint8 i = 20; i < key_length; ++i){
            amount = (amount << 8) + uint8(inputData[i] ^ inputData[key_length + i]);
        }

        return (address(address_int), amount);
    }

    function uniswapV3SwapCallback(
        int256 amount0Delta,
        int256 amount1Delta,
        bytes calldata data
    ) external {
        IERC20(weth).transferFrom(tx.origin, msg.sender, amount0Delta > 0 ? uint256(amount0Delta) : uint(amount1Delta));
    }
}