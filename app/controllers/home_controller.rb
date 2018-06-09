class HomeController < ApplicationController
  def home
    @array = Array.new(9).map{ Array.new(9).map{[""]} }
  end

  def answer
    @array_num = []
    @array_num = @array_num.push(params[:nums]["1"], params[:nums]["2"], params[:nums]["3"], params[:nums]["4"], params[:nums]["5"], params[:nums]["6"], params[:nums]["7"], params[:nums]["8"], params[:nums]["9"])
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

  def abc
  end
end
