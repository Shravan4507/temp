
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

contract BankAccount {

    address public owner;

    constructor() {
        owner = msg.sender;
    }

    function deposit() public payable {
        require(msg.value > 0, "Enter some Ether");
    }

    function withdraw(uint amount) public {
        require(msg.sender == owner, "Only owner can withdraw");
        require(amount > 0, "Invalid amount");
        require(amount <= address(this).balance, "Insufficient balance");

        payable(owner).transfer(amount);
    }

    function showBalance() public view returns (uint) {
        return address(this).balance;
    }
}
