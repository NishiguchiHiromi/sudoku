#!/usr/bin/env ruby
# -*- encoding: utf-8 -*-
require "rubypython"

def callpython
RubyPython.start


=begin
cPickle = RubyPython.import("cPickle")
p cPickle.dumps("Testing RubyPython.").rubify
dir = File.dirname(__FILE__)
sys = RubyPython.import 'sys'
sys.path.append File.join(dir, '.')
=end
called_ruby = RubyPython.import("test")
#called_ruby.print_python

#puts called_ruby.print_python_with_argument!( arg1: "Ruby String" ).rubify
#puts called_ruby.print_python_with_argument!( arg1: 1234 ).rubify

#cPickle = RubyPython.import("cPickle")
#p cPickle.dumps("Testing RubyPython.").rubify
#puts 'Pythonの自作メソッドを呼び出す'
#dir = File.dirname(__FILE__)
#sys = RubyPython.import 'sys'
#sys.path.append File.join(dir, '.')
#called_ruby = RubyPython.import("test")
return called_ruby.test().rubify


RubyPython.stop
end
