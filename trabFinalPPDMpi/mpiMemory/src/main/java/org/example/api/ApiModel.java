package org.example.api;

public class ApiModel {

    public Character[] localMemory;
    public Integer totalMemoryAllocated;

    public ApiModel() {
        this.localMemory = new Character[0];
        this.totalMemoryAllocated = 0;
    }
}
