from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from .models import Maze

def easyRedirect(request):
    return HttpResponseRedirect("/easy")


def easy(request):
    maze = Maze(8, 4, 6).createMaze()
    return render(request, 'maze/layout.html', 
        { 
            'maze': maze, 
            'keys': 6, 
            'easyClass': 'btn btn-outline-info  active',
            'mediumClass': 'btn btn-outline-info ',
            'hardClass': 'btn btn-outline-info ' 
        })

def medium(request):
    maze = Maze(8, 6, 8).createMaze()
    return render(request, 'maze/layout.html', 
        { 
            'maze': maze,
            'keys': 8,
            'easyClass': 'btn btn-outline-info ',
            'mediumClass': 'btn btn-outline-info  active',
            'hardClass': 'btn btn-outline-info ' 
         })

def hard(request):
    maze = Maze(8, 10, 10).createMaze()
    return render(request, 'maze/layout.html', 
        { 
            'maze': maze, 
            'keys': 10,
            'easyClass': 'btn btn-outline-info ',
            'mediumClass': 'btn btn-outline-info ',
            'hardClass': 'btn btn-outline-info active ' 
        })