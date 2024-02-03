// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;


interface IUniswapV3Pool {
    function swap(
    address recipient,
    bool zeroForOne,
    int256 amountSpecified,
    uint160 sqrtPriceLimitX96,
    bytes memory data
    ) external returns (int256 amount0, int256 amount1);

    function token0() external view returns (address);

    function token1() external view returns (address);
}