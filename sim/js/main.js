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

function RoomManager() {
    RoomManager.prototype.__init__.apply(this, arguments);
}
RoomManager.prototype.__init__ = function __init__(roomname){
    var self = this;
    self.room = Game.rooms[roomname];
    self.room.memory.manager = self;
    self.creeps = self.room.find(FIND_MY_CREEPS);
    self.spawn = self.room.find(FIND_MY_SPAWNS)[0];
    self.test = [];
    if (Game.time % 10 === 0) {
        __rapydscript_print(self.spawn._name);
        __rapydscript_print(dir(self.spawn));
        __rapydscript_print(self.spawn.energy);
    }
    self.spawnManager();
    self.behaviorManager();
};
RoomManager.prototype.spawnManager = function spawnManager(){
    var self = this;
    var creep;
    if (len(self.creeps) < 1) {
        creep = new BasicHarvester(self.spawn);
        creep.spawn();
    }
};
RoomManager.prototype.behaviorManager = function behaviorManager(){
    var self = this;
    var classmap, cls, behavior, behaviorClass, creep;
    classmap = {
        "BasicHarvester": BasicHarvesterBehavior
    };
    var __rapydscript_Iter3 = __rapydscript_Iterable(self.creeps);
    for (var __rapydscript_Index3 = 0; __rapydscript_Index3 < __rapydscript_Iter3.length; __rapydscript_Index3++) {
        creep = __rapydscript_Iter3[__rapydscript_Index3];
        cls = creep.memory.class;
        if (__rapydscript_in(cls, classmap)) {
            behavior = classmap[cls];
            behaviorClass = new behavior(self.room, creep);
            behaviorClass.tick();
        }
    }
};

function _Creep() {
    _Creep.prototype.__init__.apply(this, arguments);
}
"I'd call this a Creep but it breaks the game?";
_Creep.prototype.body = [];
_Creep.prototype.memory = {
    "class": "AbstractBaseCreep"
};
_Creep.prototype.name = null;
_Creep.prototype.__init__ = function __init__(spawner){
    var self = this;
    self.spawner = spawner;
};
_Creep.prototype.spawn = function spawn(){
    var self = this;
    var resp;
    resp = self.spawner.canCreateCreep(self.body, self.name);
    if (resp === OK) {
        __rapydscript_print("Spawning new " + self.type);
        __rapydscript_print("Body: " + self.body);
        __rapydscript_print("Memory: " + self.memory);
        self.spawner.createCreep(self.body, self.name, self.memory);
    } else {
        __rapydscript_print("Tried to spawn a " + self.type + " but got code " + resp);
    }
};

function BasicHarvester() {
    BasicHarvester.prototype.__init__.apply(this, arguments);
}
__rapydscript_extends(BasicHarvester, _Creep);
BasicHarvester.prototype.body = [ WORK, MOVE, CARRY ];
BasicHarvester.prototype.memory = {
    "class": "BasicHarvester"
};

function _CreepBehavior() {
    _CreepBehavior.prototype.__init__.apply(this, arguments);
}
_CreepBehavior.prototype.__init__ = function __init__(room, creep){
    var self = this;
    self.room = room;
    self.creep = creep;
    self.memory = creep.memory;
};
_CreepBehavior.prototype._get = function _get(key){
    var self = this;
    "Retrieve an object from persistent memory";
    if (__rapydscript_in(key, self.memory)) {
        return Game.getObjectById(self.memory[key]);
    }
};
_CreepBehavior.prototype._set = function _set(key, object){
    var self = this;
    "Set an object in persistent memory";
    self.memory[key] = object.id;
};

function BasicHarvesterBehavior() {
    BasicHarvesterBehavior.prototype.__init__.apply(this, arguments);
}
__rapydscript_extends(BasicHarvesterBehavior, _CreepBehavior);
BasicHarvesterBehavior.prototype.find_closest_spawn = function find_closest_spawn(){
    var self = this;
    var spawn;
    spawn = self._get("closest_spawn");
    if (!spawn) {
        spawn = self.creep.pos.findClosestByPath(FIND_MY_SPAWNS);
        self._set("closest_spawn", spawn);
    }
    return spawn;
};
BasicHarvesterBehavior.prototype.find_closest_energy = function find_closest_energy(){
    var self = this;
    var energy;
    energy = self._get("closest_energy");
    if (!energy) {
        energy = self.creep.pos.findClosestByPath(FIND_SOURCES);
        self._set("closest_energy", energy);
    }
    return energy;
};
BasicHarvesterBehavior.prototype.tick = function tick(){
    var self = this;
    var creep, energy, spawn, resp;
    creep = self.creep;
    if (_.sum(creep.carry) < creep.carryCapacity) {
        energy = self.find_closest_energy();
        resp = creep.harvest(energy);
        if (resp === ERR_NOT_IN_RANGE) {
            creep.say("going out");
            creep.moveTo(energy);
        } else {
            creep.say("harvesting");
        }
    } else {
        spawn = self.find_closest_spawn();
        resp = creep.transfer(spawn, RESOURCE_ENERGY);
        if (resp === ERR_NOT_IN_RANGE) {
            creep.say("returning");
            creep.moveTo(spawn);
        } else {
            creep.say("transferring");
        }
    }
};

__rapydscript_print = console.log;
function main() {
    var manager, room;
    var __rapydscript_Iter4 = __rapydscript_Iterable(Game.rooms);
    for (var __rapydscript_Index4 = 0; __rapydscript_Index4 < __rapydscript_Iter4.length; __rapydscript_Index4++) {
        room = __rapydscript_Iter4[__rapydscript_Index4];
        manager = new RoomManager(room);
    }
}
module.exports.loop = main();