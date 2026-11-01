
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

contract StudentData {

    struct Student {
        uint rollNo;
        string name;
        uint age;
    }

    Student[] public students;

    uint public fallbackCount;
    uint public totalReceived;

    event FallbackCalled(address sender, uint amount);

    function addStudent(uint _rollNo, string memory _name, uint _age) public {
        students.push(Student(_rollNo, _name, _age));
    }

    function getStudent(uint index) public view returns (uint, string memory, uint) {
        require(index < students.length, "Invalid index");

        Student memory s = students[index];
        return (s.rollNo, s.name, s.age);
    }

    function getStudentCount() public view returns (uint) {
        return students.length;
    }

    fallback() external payable {
        fallbackCount++;
        totalReceived += msg.value;

        emit FallbackCalled(msg.sender, msg.value);
    }
}
