require_relative 'boot'

#require 'rails/all'        #->コメントアウト
require "action_controller/railtie" #->追加
require "action_mailer/railtie"     #->追加
require "active_resource/railtie"   #->追加
require "rails/test_unit/railtie"   #->追加
require "sprockets/railtie"         #->追加

# Require the gems listed in Gemfile, including any gems
# you've limited to :test, :development, or :production.
Bundler.require(*Rails.groups)

module Sudoku
  class Application < Rails::Application
    # Initialize configuration defaults for originally generated Rails version.
    config.load_defaults 5.1
    config.autoload_paths << "#{Rails.root}/lib"
    # Settings in config/environments/* take precedence over those specified here.
    # Application configuration should go into files in config/initializers
    # -- all .rb files in that directory are automatically loaded.
  end
end
