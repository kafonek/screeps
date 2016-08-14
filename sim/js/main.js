function __rapydscript_Iterable(iterable) {
    if (Array.isArray(iterable) || iterable instanceof String || typeof iterable === "string") {
        return iterable;
    }
    return Object.keys(iterable);
}
function __rapydscript_bind(fn, thisArg) {
    var ret;
    if (fn.orig) {
        fn = fn.orig;
    }
    if (thisArg === false) {
        return fn;
    }
    ret = function() {
        return fn.apply(thisArg, arguments);
    };
    ret.orig = fn;
    return ret;
}
function range(start, stop, step) {
    var length, idx, range;
    if (arguments.length <= 1) {
        stop = start || 0;
        start = 0;
    }
    step = arguments[2] || 1;
    length = Math.max(Math.ceil((stop - start) / step), 0);
    idx = 0;
    range = new Array(length);
    while (idx < length) {
        range[idx++] = start;
        start += step;
    }
    return range;
}
function len(obj) {
    if (Array.isArray(obj) || typeof obj === "string") {
        return obj.length;
    }
    return Object.keys(obj).length;
}
function eq(a, b) {
    var i;
    "\n    Equality comparison that works with all data types, returns true if structure and\n    contents of first object equal to those of second object\n\n    Arguments:\n        a: first object\n        b: second object\n    ";
    if (a === b) {
        return true;
    }
    if (Array.isArray(a) && Array.isArray(b) || a instanceof Object && b instanceof Object) {
        if (a.constructor !== b.constructor || a.length !== b.length) {
            return false;
        }
        if (Array.isArray(a)) {
            for (i = 0; i < len(a); i++) {
                if (!eq(a[i], b[i])) {
                    return false;
                }
            }
        } else {
            var __rapydscript_Iter2 = __rapydscript_Iterable(a);
            for (var __rapydscript_Index2 = 0; __rapydscript_Index2 < __rapydscript_Iter2.length; __rapydscript_Index2++) {
                i = __rapydscript_Iter2[__rapydscript_Index2];
                if (!eq(a[i], b[i])) {
                    return false;
                }
            }
        }
        return true;
    }
    return false;
}
function __rapydscript_in(val, arr) {
    if (Array.isArray(arr) || typeof arr === "string") {
        return arr.indexOf(val) !== -1;
    } else {
        if (arr.hasOwnProperty(val)) {
            return true;
        }
        return false;
    }
}
function dir(item) {
    var arr;
    arr = [];
    for (var i in item) {
        arr.push(i);
    }
    return arr;
}
function __rapydscript_extends(child, parent) {
    child.prototype = Object.create(parent.prototype);
    child.prototype.constructor = child;
}
function __rapydscript_print() {
    if (typeof console === "object") {
        console.log.apply(console, arguments);
    }
}

var __name__ = "__main__";

function CreepManager() {
    CreepManager.prototype.__init__.apply(this, arguments);
}
CreepManager.prototype.__init__ = function __init__(roomname){
    var self = this;
    self.room = Game.rooms[roomname];
    self.creeps = self.room.find(FIND_MY_CREEPS);
    self.spawn = self.room.find(FIND_MY_SPAWNS)[0];
    if (Game.time % 10 === 0) {
        __rapydscript_print(dir(self.spawn));
        __rapydscript_print(self.spawn.energy);
    }
};
CreepManager.prototype.spawnManager = function spawnManager(){
    var self = this;
    var creep;
    if (len(self.creeps) < 2) {
        creep = new Creep(self.spawn);
    }
};

function Creep() {
    Creep.prototype.__init__.apply(this, arguments);
}
Creep.prototype.__init__ = function __init__(spawner){
    var self = this;
    self.spawner = spawner;
    __rapydscript_print(self.spawner);
    self.body = [ WORK, MOVE, CARRY ];
};
Creep.prototype.spawn = function spawn(){
    var self = this;
    var resp;
    resp = self.spawner.canCreateCreep(self.body);
    __rapydscript_print(resp);
};

function BasicHarvester() {
    BasicHarvester.prototype.__init__.apply(this, arguments);
}
__rapydscript_extends(BasicHarvester, Creep);


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

__rapydscript_print = console.log;
function main() {
    var manager, room;
    if (Game.time % 5 === 0) {
        __rapydscript_print(Game.time);
    }
    var __rapydscript_Iter3 = __rapydscript_Iterable(Game.rooms);
    for (var __rapydscript_Index3 = 0; __rapydscript_Index3 < __rapydscript_Iter3.length; __rapydscript_Index3++) {
        room = __rapydscript_Iter3[__rapydscript_Index3];
        manager = new CreepManager(room);
    }
}
module.exports.loop = main();