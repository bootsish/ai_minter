//SPDX-License-Identifier: GPL-3.0

pragma solidity ^0.5.0;

import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/release-v2.5.0/contracts/token/ERC721/ERC721Full.sol";

contract artRegistry is ERC721Full {

    constructor() public ERC721Full("ArtRegistryToken", "ART") {}

    struct ArtWork {
        string name;
        string artist;
        uint appraisalValue;
        string tokenJSON;
    }

    mapping(uint => ArtWork) public artCollection; 

    function registerArtWork(
                            address owner,
                            string memory name,
                            string memory artist, 
                            uint appraisalValue,
                            string memory tokenURI,
                            string memory tokenJSON
                            ) public returns (uint) {
                                        uint tokenID = totalSupply();
                                        _mint(owner,tokenID);
                                        _setTokenURI(tokenID, tokenURI);
                                        artCollection[tokenID] = ArtWork(name, artist, appraisalValue, tokenJSON);
                    return tokenID;   
    }

    function newAppraisal(
                            uint tokenID,
                            uint appraisalValue,
                            string memory tokenURI,
                            string memory tokenJSON
        ) public returns(uint) {
            artCollection[tokenID].appraisalValue = appraisalValue; 
            emit Appraisal(tokenID, appraisalValue, tokenURI, tokenJSON);
            return artCollection[tokenID].appraisalValue;
    }

    event Appraisal (uint tokenID, uint appraisalValue, string tokenURI, string tokenJSON);

    function imageURI(uint tokenID) public view returns (string memory) {
        return artCollection[tokenID].tokenJSON;
    }



}
