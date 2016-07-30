
var __name__ = "__main__";

function main() {
    var creep;
    var ՐՏ_Iter1 = ՐՏ_Iterable(Game.creeps);
    for (var ՐՏ_Index1 = 0; ՐՏ_Index1 < ՐՏ_Iter1.length; ՐՏ_Index1++) {
        creep = ՐՏ_Iter1[ՐՏ_Index1];
        roleHarvester.run(creep);
    }
}
module.exports.loop = main();
function roleHarvester() {
}
roleHarvester.prototype.run = function run(creep){
    var self = this;
    var energy_source;
    if (creep.carry.energy > creep.carryCapacity) {
        energy_source = creep.room.find(FIND_SOURCES)[0];
        if (creep.harvest(energy_source) === ERR_NOT_IN_RANGE) {
            creep.moveTo(energy_source);
        } else {
            if (creep.transfer(Game.spawns["Spawn1"], RESOURCE_ENERGY) === ERR_NOT_IN_RANGE) {
                creep.moveTo(Game.spawns["Spawn1"]);
            }
        }
    }
};
