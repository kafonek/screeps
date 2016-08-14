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
            var __rapydscript_Iter3 = __rapydscript_Iterable(a);
            for (var __rapydscript_Index3 = 0; __rapydscript_Index3 < __rapydscript_Iter3.length; __rapydscript_Index3++) {
                i = __rapydscript_Iter3[__rapydscript_Index3];
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
CreepManager.prototype.__init__ = function __init__(room){
    var self = this;
    self.room = room;
    __rapydscript_print("CreepManager spawned");
};
CreepManager.prototype.print_creeps = function print_creeps(){
    var self = this;
    __rapydscript_print("There are");
};

__rapydscript_print = console.log;
function main() {
    var manager, name;
    if (Game.time % 5 === 0) {
        __rapydscript_print(Game.time);
    }
    var __rapydscript_Iter4 = __rapydscript_Iterable(Game.rooms);
    for (var __rapydscript_Index4 = 0; __rapydscript_Index4 < __rapydscript_Iter4.length; __rapydscript_Index4++) {
        name = __rapydscript_Iter4[__rapydscript_Index4];
        manager = CreepManager(Game.rooms[name]);
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
