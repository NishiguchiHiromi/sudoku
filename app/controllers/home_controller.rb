class HomeController < ApplicationController
  def home
    @nums={1 =>1}
    @array=Array.new(9).map{ Array.new(9).map{[""]} }
  end
  def answer
    @array_num=[]
    @nums=params[:nums]
    @array_num=@array_num.push(@nums["1"],@nums["2"],@nums["3"],@nums["4"],@nums["5"],@nums["6"],@nums["7"],@nums["8"],@nums["9"])
    require "rubypython"
    RubyPython.start
    dir = File.dirname(__FILE__)
    sys = RubyPython.import 'sys'
    sys.path.append File.join(dir, '.')
    called_ruby = RubyPython.import("sudokutest")
    @array=called_ruby.answer(@array_num).rubify
    RubyPython.stop
    render :home
  end
end
